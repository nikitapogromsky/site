FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir flask
COPY . .

RUN chmod +x startup.sh

ENTRYPOINT ["bash"]
CMD ["./startup.sh"]
