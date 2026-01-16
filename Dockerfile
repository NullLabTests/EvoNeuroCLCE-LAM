FROM python:3.12-slim
WORKDIR /app
COPY src/ .
RUN pip install --quiet sympy networkx torch gymnasium pytest matplotlib transformers  # No deprecations
CMD ["python", "seed.py"]
