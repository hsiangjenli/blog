cd ./source/_posts/; files=$(find . -name "*.md")

echo $files

cd ../../

for file in $files; do
    uv run --locked python scripts/math_underscore_replace.py -f "$file"
done