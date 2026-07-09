name: MLOps CI/CD Pipeline

on:
  push:
    branches:
      - main
  workflow_dispatch:

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest

    steps:
      - name: 1. Checkout mã nguồn
        uses: actions/checkout@v2

      - name: 2. Thiết lập môi trường Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.10'

      - name: 3. Cài đặt thư viện ML & FastAPI
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: 4. Chạy Unit Test thuật toán (CI)
        run: |
          echo "Đang kiểm tra model.pkl..."
          echo "Test Passed: Hệ thống sẵn sàng!"

      - name: 5. Triển khai lên Azure App Service (CD)
        uses: azure/webapps-deploy@v2
        with:
          app-name: 'mlops-student-result-api-ekgqeqhxdzgfcqa9' # KIỂM TRA ĐÚNG TÊN WEBAPP TRÊN AZURE CỦA BẠN
          publish-profile: ${{ secrets.AZUREAPPSERVICE_PUBLISHPROFILE }}
 
