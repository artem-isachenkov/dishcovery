from fastapi import APIRouter

from dependencies import SupabaseDep


router = APIRouter(prefix="/recipes", tags=["recipes"])


@router.get("/")
async def get_recipes(supabase: SupabaseDep):
    return supabase.table("recipe").select("*", "category(*)").execute()


@router.get("/{recipe_id}")
async def get_recipe(recipe_id: int, supabase: SupabaseDep):
    return (
        supabase.table("recipe")
        .select("*", "category(*)")
        .eq("id", recipe_id)
        .single()
        .execute()
        .data
    )
