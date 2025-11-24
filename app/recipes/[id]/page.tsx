// "use client";
// import { useParams } from "next/navigation";
// import { useRouter } from "next/router";

import { fetchRecipe } from "@/lib/actions";

type Params = {
  id: number;
};

type RecipeProps = {
  params: Promise<Params>;
};

export default async function Recipe(props: RecipeProps) {
  const { id } = await props.params;
  const recipe = await fetchRecipe(id);

  // const { id } = useParams();
  // const router = useRouter();
  return (
    <div>
      <h1>Recipe: {id}</h1>
      <div>{JSON.stringify(recipe)}</div>
    </div>
  );
}
