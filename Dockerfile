FROM python:3.9

WORKDIR /app
COPY . .
ENV PYTHONPATH "."

RUN python3.9 -m pip install -r requirements.txt

ENTRYPOINT ["python3.9"]
CMD ["src/main.py"]