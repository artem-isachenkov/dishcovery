import { fetchCategories } from "@/lib/actions";
import Link from "next/link";

export default async function CategoriesPage() {
  const categories = await fetchCategories();

  return (
    <div>
      <ul>
        {categories.data.map((category) => (
          <li key={category.id}>
            <Link href={`/categories/${category.id}`}>{category.name}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
}
