# !/bin/bash

LOG_FILE="../logs/update.log"

echo "========== UPDATE ============" | tee -a $LOG_FILE
echo "Nodo: ${hostname}" | tee -a $LOG_FILE

echo "[INFO] Buscando actualizaciones..." | tee -a $LOG_FILE
sleep 1

echo "[INFO] Descargando paquetes..." | tee -a $LOG_FILE
sleep 1

echo "[INFO] Instalando paquetes..." | tee -a $LOG_FILE
sleep 1

echo "[SUCCESS] Sistema actualizado" | tee -a $LOG_FILE
echo "-----------------------------------" | tee -a $LOG_FILE

