# !/bin/bash

LOG_FILE="../logs/deploy.log"

echo "========== DEPLOY ==========" | tee -a $LOG_FILE 
echo "Nodo: ${hostname}" | tee -a $LOG_FILE
echo "[INFO] Iniciando despliegue de aplicación..." | tee -a $LOG_FILE

for i in {1..3}
do 
    echo "[PROGRESS] Paso $i/3 ejecutando..." | tee -a $LOG_FILE
    sleep 1
done

echo "[INFO] Instalando dependencias..." | tee -a $LOG_FILE
sleep 1

echo "[INFO] Reiniciando servicio..." | tee -a $LOG_FILE
sleep 1

echo "[SUCCESS] Deploy completado" | tee -a $LOG_FILE
echo "-----------------------------------------" | tee -a $LOG_FILE