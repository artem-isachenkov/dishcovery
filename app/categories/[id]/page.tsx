type Params = {
  id: number;
};

type CategoryProps = {
  params: Promise<Params>;
};

export default async function Category(props: CategoryProps) {
  const { id } = await props.params;
  return (
    <div>
      <h1>Category: {id}</h1>
    </div>
  );
}
