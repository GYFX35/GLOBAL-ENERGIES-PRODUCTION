from fastapi import FastAPI
from src.modeling.optimization import solve_biomass_optimization

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Global Energy Access API!"}

@app.post("/optimize")
def run_optimization():
    res = solve_biomass_optimization()
    # Convert the result to a JSON-serializable format
    result_dict = {
        "cost": res.fun,
        "solution_kg": res.x.tolist() if res.success else [],
        "success": res.success,
        "message": res.message
    }
    return result_dict
