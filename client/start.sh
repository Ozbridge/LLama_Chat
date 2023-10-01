docker build -t image_api ./..
docker run -dp 8080:8080 -v ./models:/app/models image_api

pip3 install streamlit
pip3 install requests

streamlit run client_v2.py --server.port 8010

open https://localhost:8010



