# app/routes/views.py


@router.get("/api_a/{num}", tags=["api_a"])
async def view_a(num: int, auth=Depends(get_current_user)) -> Dict[str, int]:
    return main_func_a(num)