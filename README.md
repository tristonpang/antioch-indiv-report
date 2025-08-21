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
