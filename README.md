# Antioch21 CMRA Individual Report Generation Server

## Development

```
# Mount the venv (from within the repo directory)
source indiv-report-env/bin/activate

# Test report generation using dev_test.py
# Requires the example-webhook-response.json file
# Comment out or include the gmail_send_message call to omit or test email sending
python3 dev_test.py
```

## Usage

```
flask run -p <PORT_NUMBER>
```

## Deployment (after ssh into the droplet)

1. Pull codebase into DigitalOcean droplet
2. Build docker image

```
docker build -t indiv-report .
```

3. Run docker container

```
docker run -p 8080:8080 indiv-report
```

4. Exec into the docker container (view container id via `docker ps`)

```
docker exec -it <container_id> /bin/sh
```

5. Install remaining dependencies

```
plotly_get_chrome

apt-get install libnss3 libatk-bridge2.0-0 libcups2 libxcomposite1 libxdamage1 libxfixes3 libxrandr2 libgbm1 libxkbcommon0 libpango-1.0-0 libcairo2 libasound2
```

6. Login to gmail account using dev_test.py
