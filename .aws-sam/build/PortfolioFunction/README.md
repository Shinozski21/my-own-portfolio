# my-own-portfolio

## Local development

- Create a virtual environment and install dependencies: `python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt`.
- Run the Flask dev server: `python main.py`.
- Static assets live under `static/`; templates are in `templates/`.

## Deploying on AWS Lambda (via API Gateway)

1. Ensure dependencies are installed locally (`pip install -r requirements.txt`).
2. Package the application for Lambda (for example with AWS SAM, Serverless Framework, or Zappa). The Lambda entry point is `lambda_handler.handler`, which uses the `aws-wsgi` adapter to run the Flask app on Lambda.
3. Deploy the packaged artifact to AWS Lambda and connect it to an HTTP API or REST API Gateway stage.
4. Set environment variables as needed (`FLASK_ENV=production`, etc.).

## Custom domain with Route 53

- Request a free TLS certificate in AWS Certificate Manager in the same region as your API Gateway.
- Create a custom domain in API Gateway and attach the ACM certificate, mapping it to the deployed stage.
- In Route 53, add an alias `A` record pointing to the API Gateway custom domain.
