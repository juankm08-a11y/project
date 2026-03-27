from parser.grammar.DevOpsDSLVisitor import DevOpsDSLVisitor

class Interpreter(DevOpsDSLVisitor):

    def __init__(self, executor):
        self.executor = executor

    # =========================
    # PROGRAM
    # =========================
    
    def visitProgram(self, ctx):
        print("[INFO] Iniciando ejecución del programa DSL\n")

        for stmt in ctx.statement():
            self.visit(stmt)

        print("\n[INFO] Ejecución finalizada")
    
    # =========================
    # COMMANDS
    # =========================
    
    def visitNodeCommand(self, ctx):
        node = ctx.ID().getText()
        script = ctx.STRING().getText().strip('"')

        print(f"[DSL] Ejecutar en nodo: {node} -> {script}")
        self.executor.run_on_node(node, script)

    def visitGroupCommand(self, ctx):
        group = ctx.ID().getText()

        print(f"[DSL] Actualizar grupo: {group}")
        self.executor.update_group(group)

    def visitDeployCommand(self, ctx):
        app = ctx.ID(0).getText()
        group = ctx.ID(1).getText()

        print(f"[DSL] Deploy '{app}' en '{group}'")
        self.executor.deploy(app, group)

    
    # =========================
    # RULES
    # =========================
    
    def visitRule(self, ctx):
        print("[DSL] Evaluando regla...")

        if self.evaluate_condition(ctx.condition()):
            print("[DSL] Condición verdadera\n")
            self.visit(ctx.action())
        else:
            print("[DSL] Condición falsa\n")

    def evaluate_condition(self, ctx):
        node = ctx.ID(0).getText()
        metric = ctx.ID(1).getText()
        operator = ctx.comparator().getText()
        value = int(ctx.NUMBER().getText())

        data = self.executor.get_sensor_data(node)
        current = data.get(metric, 0)

        if operator == ">":
            return current > value
        elif operator == "<":
            return current < value
        elif operator == "==":
            return current == value
        elif operator == ">=":
            return current >= value
        elif operator == "<=":
            return current <= value

        return False
    
    # =========================
    # ACTIONS
    # =========================

    def visitAction(self, ctx):
        if ctx.getChildCount() == 3:
            print(f"[ACTION] {ctx.ID().getText()}")

        elif ctx.STRING():
            node = ctx.ID().getText()
            script = ctx.STRING().getText().strip('"')

            self.executor.run_on_node(node, script)

    # =========================
    # PARALLEL
    # =========================
    
    def visitParallelBlock(self, ctx):
        import threading

        print("[DSL] Ejecutando paralelo\n")

        threads = []

        for stmt in ctx.statement():
            t = threading.Thread(target=self.visit, args=(stmt,))
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

        print("\n[DSL] Fin paralelo")