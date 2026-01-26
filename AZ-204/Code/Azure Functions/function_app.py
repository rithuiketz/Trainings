from azure.functions import HttpMethod,TriggerApi,HttpRequest,HttpResponse
import azure.functions as func


app  = func.FunctionApp()

@app.function_name(name="HttpTrigger1")
@app.route(route="/test")
def main(req: HttpRequest) -> str:
    user = req.params.get("user")
    return f"Hello, {user}!"