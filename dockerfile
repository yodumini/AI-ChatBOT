# 使用輕量級的Python映像作為基礎
FROM python:3.9

# 設置工作目錄
WORKDIR /app

# 複製當前目錄下的所有文件到容器中的工作目錄
COPY . .

# 使用ARG接收建置時環境變數
ARG BUILDTIME_ENV_EXAMPLE
ENV BUILDTIME_ENV_EXAMPLE=${BUILDTIME_ENV_EXAMPLE}

# 安裝依賴
RUN pip install --no-cache-dir -r requirements.txt

# 暴露容器運行時的端口號
EXPOSE 8080

# 配置環境變數
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8080

# 配置容器啟動後執行的命令
CMD ["flask", "run"]
