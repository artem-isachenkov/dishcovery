from fastapi import APIRouter

from dependencies import SupabaseDep


router = APIRouter(prefix="/categories", tags=["categories"])


@router.get("/")
async def get_recipes(supabase: SupabaseDep):
    return supabase.table("category").select("*").execute()


@router.get("/{category_id}")
async def get_recipe(category_id: int, supabase: SupabaseDep):
    return (
        supabase.table("category")
        .select("*")
        .eq("id", category_id)
        .single()
        .execute()
        .data
    )
