# FUCKING CV GENERATOR

Magic not in the making? Yes? No? Hello? Bye?

![](/docs/sample.png)

### Getting Started
1. Edit your CV in bio.md
2. Deployment
3. Open the bio.html in your browser
4. Print the page as PDF, uncheck `Print headers and footers` and `Print Background`, Adjust the scale
5. Done


## Deployment
### via Nix
```nix
nix-shell --command "python generate.py"
```
### via Python
```bash
pip install markdown
python3 generate.py
```