import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from antlr4 import *
from antlr4.error.ErrorListener import ConsoleErrorListener

from parser.grammar.DevOpsDSLLexer import DevOpsDSLLexer
from parser.grammar.DevOpsDSLParser import DevOpsDSLParser

from interpreter.interpreter import Interpreter
from executor.executor import Executor


def main():
    print("[INFO] Iniciando sistema DSL...\n")

    # Damos permisos para pasar archivo por argumento
    file = "script.dsl"
    if len(sys.argv) > 1:
        file = sys.argv[1]

    # Validamo que el archivo existe
    if not os.path.exists(file):
        print(f"[ERROR] No existe el archivo: {file}")
        return
    
    # Cargamos el archivos DSL
    input_stream = FileStream(file)

    # Lexer
    lexer = DevOpsDSLLexer(input_stream)

    # Creamos los tokens
    tokens = CommonTokenStream(lexer)
    tokens.fill()

    # Mostramos los Tokens
    print("[TOKENS]")
    for token in tokens.tokens:
        print(token)

    # Parser
    parser = DevOpsDSLParser(tokens)

    # Manejo de errores sintácticos
    parser.removeErrorListeners()
    parser.addErrorListener(ConsoleErrorListener())

    # Tree
    tree = parser.program()

    # Mostramos el arbol sintáctico
    print("\n[ÁRBOL]")
    print(tree.toStringTree(recog=parser))

    # Mostramos errores sintácticos
    print("\nErrores sintácticos:", parser.getNumberOfSyntaxErrors())

    print("\n[INFO] Árbol sintáctico generado\n")

    # Inicializamos el sistema
    executor = Executor()
    interpreter = Interpreter(executor)

    # Ejecutamos 
    interpreter.visit(tree)


if __name__ == "__main__":
    main()