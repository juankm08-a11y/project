# !/bin/bash

echo "========== DEPLOY =========="
echo "Nodo: ${hostname}"
echo "[INFO] Iniciando despliegue..."

for i in {1..3}
do 
    echo "[PROGRESS] Paso $i/3..."
    sleep 1
done

echo "[SUCCESS] Deploy completado"

