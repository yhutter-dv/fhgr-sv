# FHGR Scientific Visualization

## Python Setup
Please run the following command to install all necessary packages

```bash
python -m venv ./venv
pip install -r ./requirements.txt
```

## Documentation
As a base template the awesome pandoc-latex-template from [Wandmalfarbe](https://github.com/Wandmalfarbe/pandoc-latex-template) was used.

### Onetime Setup
First make sure pandoc and the necessary latex packages are installed:
```bash
sudo pacman -S pandoc texlive
```

### Build Documentation
In order to generate the documentation simply make the `doc.sh` file executable and run it:
```bash
cd doc
chmod +x doc.sh
./doc.sh
```
