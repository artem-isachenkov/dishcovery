import { Recipes } from "@/components/recipes";
import { fetchRecipes } from "@/lib/actions";

export default async function RecipesPage() {
  const recipes = await fetchRecipes();
  return <Recipes recipes={recipes.data} />;
}
