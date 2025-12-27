# ---------- BUILDER ----------
FROM python:3.11-slim AS builder
WORKDIR /app

COPY app/requirements.txt .
RUN pip install --user -r requirements.txt

COPY app/ app/

# ---------- TEST ----------
FROM builder AS test
WORKDIR /app
RUN pytest -q

# ---------- FINAL ----------
FROM python:3.11-slim AS final
WORKDIR /app

COPY --from=builder /root/.local /root/.local
ENV PATH="/root/.local/bin:$PATH"

COPY app/ app/

CMD ["python", "src/app.py"]
