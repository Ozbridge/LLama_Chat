# LLama-Gita

### How to run
- Download the model file from this [link](https://drive.google.com/file/d/1CD-OdFQlX4_6HHQJ0U7pEOkDHlxGmmmk/view?usp=sharing) and place in LLama_Chat/client/models
- Open the terminal with LLama_Chat/client as the current directory
- Run ./start.sh
- It can take upto 5 min to build the image and start the server depending on the specifications. Response generation also take approx 2 min per response.

### Made using llama.cpp

- API server is containerized, with endpoint at http://127.0.0.1:8080

- client_v2.py simply access the given endpoint to obtain results and is replaceable.


