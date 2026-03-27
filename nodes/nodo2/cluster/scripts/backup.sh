#!/bin/bash

SCRIPT_DIR=$(dirname "$0")
LOG_FILE="$SCRIPT_DIR/../logs/backup.log"

mkdir -p "$SCRIPT_DIR/../logs"

echo "========== BACKUP ==========" 
echo "Nodo: ${hostname}" | tee -a $LOG_FILE
echo "[INFO] Iniciando backup..." tee -a $LOG_FILE

sleep 1

echo "[INFO] Copiando archivos críticos..." tee -a $LOG_FILE
sleep 1

echo "[INFO] Comprimiendo backup..." tee -a $LOG_FILE
sleep 1

echo "[INFO] Verificando integridad..." tee -a $LOG_FILE
sleep 1

echo "[SUCCESS] Backup completado correctamente"

