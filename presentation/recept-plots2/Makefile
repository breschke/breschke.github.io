## Put this Makefile in your project directory---i.e., the directory
## containing the paper you are writing. Assuming you are using the
## rest of the toolchain here, you can use it to create .html, .tex,
## and .pdf output files (complete with bibliography, if present) from
## your markdown file.
## -	Change the paths at the top of the file as needed.
## -	Using `make` without arguments will generate html, tex, and pdf
## 	output files from all of the files with the designated markdown
##	extension. The default is `.md` but you can change this.
## -	You can specify an output format with `make tex`, `make pdf` or
## - 	`make html`.
## -	Doing `make clean` will remove all the .tex, .html, and .pdf files
## 	in your working directory. Make sure you do not have files in these
##	formats that you want to keep!

## Markdown extension (e.g. md, markdown, mdown).
MEXT = md

## All markdown files in the working directory
SRC = $(wildcard *.$(MEXT))

## Location of Pandoc support files.
PREFIX = /Users/brianreschke/.pandoc

## Location of your working bibliography file
BIB = /Users/brianreschke/Dropbox/bpr/Dissertation/bib/current.bib

## CSL stylesheet (located in the csl folder of the PREFIX directory).
CSL = apsa


# PDFS=$(SRC:.md=.pdf)
HTML=$(SRC:.md=.html)
TEX=$(SRC:-final.md=.tex)


# all:	$(PDFS) $(HTML) $(TEX)
all: $(TEX)

# pdf:	clean $(PDFS)
# html:	clean $(HTML)
tex:	clean $(TEX)

# %.html:	%.md
# 	pandoc -r markdown+simple_tables+table_captions+yaml_metadata_block -w html -S --template=$(PREFIX)/templates/html.template --css=$(PREFIX)/marked/kultiad-serif.css --filter pandoc-citeproc --csl=$(PREFIX)/csl/$(CSL).csl --bibliography=$(BIB) -o $@ $<

# %.tex:	%.md
# 	gpp -H -x -DTEX=1 --include ./aux/macros.gpp $< | pandoc -r markdown+lists_without_preceding_blankline+yaml_metadata_block+fancy_lists -w latex -s -S --latex-engine=pdflatex --template=./aux/xelatex.template --filter pandoc-citeproc --csl=$(PREFIX)/csl/$(CSL).csl --bibliography=$(BIB) --number-sections -o $@
# 	if [ -f $*.lof ]; then python ~/dt1/common/loffix.py $*.lof; fi
# 	if [ -f $*.lot ]; then python ~/dt1/common/lotfix.py $*.lot; fi
# 	xelatex -shell-escape $@

%.tex:	%.md
	gpp -H -x -DTEX=1 --include ./aux/macros.gpp $< > $*-final.md
	sed -i '' -n '/---/,$$p' $*-final.md

	# reveal-md $< -w --reveal-template ./css/reveal-alt-template.html --theme black-custom --static $*
	# reveal-md $< --reveal-template ./css/reveal-alt-template.html --theme black-custom --print $*.pdf

	# gpp -H -x -DTEX=1 --include ./aux/macros.gpp $< | pandoc -r markdown+lists_without_preceding_blankline+yaml_metadata_block+fancy_lists -w latex -s -S --latex-engine=pdflatex --template=./aux/xelatex.template --filter pandoc-citeproc --csl=$(PREFIX)/csl/$(CSL).csl --bibliography=$(BIB) --number-sections -o $@
	# if [ -f $*.lof ]; then python ~/dt1/common/loffix.py $*.lof; fi
	# if [ -f $*.lot ]; then python ~/dt1/common/lotfix.py $*.lot; fi
	# xelatex -shell-escape $@

clean:
# rm -f *.html *.pdf *.tex
	rm -f *.html *.tex
