## Put this Makefile in your project directory---i.e., the directory
## containing the paper you are writing. Assuming you are using the
## rest of the toolchain here, you can use it to create .html, .tex,
## and .pdf output files (complete with bibliography, if present) from
## your markdown file.
## -	Change the paths at the top of the file as needed.
## -	Using `make` without arguments will proverate html, tex, and pdf
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
# PREFIX = /Users/brianreschke/.pandoc

## Location of your working bibliography file
BIB = /Users/brianreschke/Dropbox/bpr/Dissertation/bib/current.bib

## CSL stylesheet (located in the csl folder of the PREFIX directory).
CSL = apsa
# CSL = international-journal-of-electronic-commerce

HTML=$(SRC:.md=.html)

# all:	$(PDFS) $(HTML) $(TEX)
all: clean $(HTML)

# html:	clean $(HTML)
html: $(HTML)

%.html:	%.md
	sed -i '' "s/lastmod.*/lastmod: "$(MODTIME)"/" $*.md
	gpp -H -x -DTEX=1 --include ./aux/macros.gpp $< | pandoc -r markdown+lists_without_preceding_blankline+simple_tables+table_captions+yaml_metadata_block -w html -S --template=./aux/html.template --css=./aux/kultiad-serif.css --filter pandoc-citeproc --csl=./aux/$(CSL).csl --bibliography=$(BIB) -o $@
	# sed ':a;N;$!ba;s/---/GGG/2' $< > tmp.md
	# sed ':a;N;$!ba;s/\n/YYY/g' $< | sed 's/---/GGG/2'> tmp
	# paste -d QT -s $< > tmp
	# cat $< | tr '\r\n' '~'
	cat $< | tr '\r\n' '~' | sed -E 's/~---.*/~---/' | tr '~' '\n' > $*-tmp.html
	cat $@ >> $*-tmp.html
	sed -i '' "s/draft: true/draft: false/" $*-tmp.html
	# sed '/>1000</{s/\(citation\">\)(\([^<]*\)\(<[^>]*>\)1000/\1(\3\2/;}' $*-tmp2.html > $*-tmp3.html
	# sed '/>1000</{s/\(citation\">\)(\([^<]*\)\(<[^>]*>\)1000<\/a>, \([^)]*)\)/\1(\3\2\4<\/a>/;}' $*-tmp2.html > $*-tmp3.html
	# sed -i '' '/>1000</{s/\(citation\">\)(\([^<]*\)\(<a href=\"\)\([^-]*-\)\([^.]*\)\.\([^\"]*\)">1000<\/a>, \([^:]*\):\([^)]*\))/\1(\3https:\/\/www.lds.org\/scriptures\/\5\/\6\/\7\.\8\?lang=eng#\8">\2\7:\8<\/a>)/g;}' $*-tmp.html
	python ./aux/linkfix.py $*-tmp.html $*
	sed -i '' '/^<!DOCTYPE*/,/^<\/header>/{/^#/!{/^&/!d;};}' $*-tmp.html
	sed 's/ 1000.//g' $*-tmp.html > $@
	rm $*-tmp.html

clean:
	rm -f *.html *.pdf *.tex
