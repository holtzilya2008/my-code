FROM python:3.13-slim

COPY requirements.txt .

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

ENTRYPOINT ["pytest"]

# Arguments for the Entrypoint
CMD ["-v", "-s"]