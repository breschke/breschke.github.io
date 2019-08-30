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
# all: clean $(HTML)

# html:	clean $(HTML)
html: $(HTML)

%.html:	%.md
	gpp -H -x -DTEX=1 --include ./aux/macros.gpp $< | pandoc -r markdown+lists_without_preceding_blankline+simple_tables+table_captions+yaml_metadata_block -w html -smart --template=./aux/html.template --css=./aux/kultiad-serif.css --filter pandoc-citeproc --csl=./aux/$(CSL).csl --bibliography=$(BIB) -o $@
	# sed ':a;N;$!ba;s/---/GGG/2' $< > tmp.md
	# sed ':a;N;$!ba;s/\n/YYY/g' $< | sed 's/---/GGG/2'> tmp
	# paste -d QT -s $< > tmp
	# cat $< | tr '\r\n' '~'
	cat $< | tr '\r\n' '~' | sed -E 's/~---.*/~---/' | tr '~' '\n' > $*-tmp.html
	cat $@ >> $*-tmp.html
	sed -i '' "s/ref-1-ne/ref-bofm.1-ne/" $*-tmp.html
	sed -i '' "s/ref-2-ne/ref-bofm.2-ne/" $*-tmp.html
	sed -i '' "s/ref-jacob/ref-bofm.jacob/" $*-tmp.html
	sed -i '' "s/ref-enos/ref-bofm.enos/" $*-tmp.html
	sed -i '' "s/ref-jarom/ref-bofm.jarom/" $*-tmp.html
	sed -i '' "s/ref-omni/ref-bofm.omni/" $*-tmp.html
	sed -i '' "s/ref-w-of-m/ref-bofm.w-of-m/" $*-tmp.html
	sed -i '' "s/ref-msh/ref-bofm.mosiah/" $*-tmp.html
	sed -i '' "s/ref-alma/ref-bofm.alma/" $*-tmp.html
	sed -i '' "s/ref-hel/ref-bofm.hel/" $*-tmp.html
	sed -i '' "s/ref-3-ne/ref-bofm.3-ne/" $*-tmp.html
	sed -i '' "s/ref-4-ne/ref-bofm.4-ne/" $*-tmp.html
	sed -i '' "s/ref-morm/ref-bofm.morm/" $*-tmp.html
	sed -i '' "s/ref-ether/ref-bofm.ether/" $*-tmp.html
	sed -i '' "s/ref-moro/ref-bofm.moro/" $*-tmp.html
	sed -i '' "s/ref-dc/ref-dc-testament.dc/" $*-tmp.html
	sed -i '' "s/ref-gen/ref-ot.gen/" $*-tmp.html
	sed -i '' "s/ref-ex/ref-ot.ex/" $*-tmp.html
	sed -i '' "s/ref-lev/ref-ot.lev/" $*-tmp.html
	sed -i '' "s/ref-num/ref-ot.num/" $*-tmp.html
	sed -i '' "s/ref-deut/ref-ot.deut/" $*-tmp.html
	sed -i '' "s/ref-josh/ref-ot.josh/" $*-tmp.html
	sed -i '' "s/ref-judg/ref-ot.judg/" $*-tmp.html
	sed -i '' "s/ref-ruth/ref-ot.ruth/" $*-tmp.html
	sed -i '' "s/ref-1-sam/ref-ot.1-sam/" $*-tmp.html
	sed -i '' "s/ref-2-sam/ref-ot.2-sam/" $*-tmp.html
	sed -i '' "s/ref-1-kgs/ref-ot.1-kgs/" $*-tmp.html
	sed -i '' "s/ref-2-kgs/ref-ot.2-kgs/" $*-tmp.html
	sed -i '' "s/ref-1-chr/ref-ot.1-chr/" $*-tmp.html
	sed -i '' "s/ref-2-chr/ref-ot.2-chr/" $*-tmp.html
	sed -i '' "s/ref-ezra/ref-ot.ezra/" $*-tmp.html
	sed -i '' "s/ref-neh/ref-ot.neh/" $*-tmp.html
	sed -i '' "s/ref-esth/ref-ot.esth/" $*-tmp.html
	sed -i '' "s/ref-job/ref-ot.job/" $*-tmp.html
	sed -i '' "s/ref-ps/ref-ot.ps/" $*-tmp.html
	sed -i '' "s/ref-prov/ref-ot.prov/" $*-tmp.html
	sed -i '' "s/ref-eccl/ref-ot.eccl/" $*-tmp.html
	sed -i '' "s/ref-song/ref-ot.song/" $*-tmp.html
	sed -i '' "s/ref-isa/ref-ot.isa/" $*-tmp.html
	sed -i '' "s/ref-jer/ref-ot.jer/" $*-tmp.html
	sed -i '' "s/ref-lam/ref-ot.lam/" $*-tmp.html
	sed -i '' "s/ref-ezek/ref-ot.ezek/" $*-tmp.html
	sed -i '' "s/ref-hosea/ref-ot.hosea/" $*-tmp.html
	sed -i '' "s/ref-joel/ref-ot.joel/" $*-tmp.html
	sed -i '' "s/ref-amos/ref-ot.amos/" $*-tmp.html
	sed -i '' "s/ref-obad/ref-ot.obad/" $*-tmp.html
	sed -i '' "s/ref-jonah/ref-ot.jonah/" $*-tmp.html
	sed -i '' "s/ref-micah/ref-ot.micah/" $*-tmp.html
	sed -i '' "s/ref-nahum/ref-ot.nahum/" $*-tmp.html
	sed -i '' "s/ref-hab/ref-ot.hab/" $*-tmp.html
	sed -i '' "s/ref-zeph/ref-ot.zeph/" $*-tmp.html
	sed -i '' "s/ref-hag/ref-ot.hag/" $*-tmp.html
	sed -i '' "s/ref-zech/ref-ot.zech/" $*-tmp.html
	sed -i '' "s/ref-mal/ref-ot.mal/" $*-tmp.html
	sed -i '' "s/ref-matt/ref-nt.matt/" $*-tmp.html
	sed -i '' "s/ref-mark/ref-nt.mark/" $*-tmp.html
	sed -i '' "s/ref-luke/ref-nt.luke/" $*-tmp.html
	sed -i '' "s/ref-john/ref-nt.john/" $*-tmp.html
	sed -i '' "s/ref-acts/ref-nt.acts/" $*-tmp.html
	sed -i '' "s/ref-rom/ref-nt.rom/" $*-tmp.html
	sed -i '' "s/ref-1-cor/ref-nt.1-cor/" $*-tmp.html
	sed -i '' "s/ref-2-cor/ref-nt.2-cor/" $*-tmp.html
	sed -i '' "s/ref-gal/ref-nt.gal/" $*-tmp.html
	sed -i '' "s/ref-eph/ref-nt.eph/" $*-tmp.html
	sed -i '' "s/ref-philip/ref-nt.philip/" $*-tmp.html
	sed -i '' "s/ref-col/ref-nt.col/" $*-tmp.html
	sed -i '' "s/ref-1-thes/ref-nt.1-thes/" $*-tmp.html
	sed -i '' "s/ref-2-thes/ref-nt.2-thes/" $*-tmp.html
	sed -i '' "s/ref-1-tim/ref-nt.1-tim/" $*-tmp.html
	sed -i '' "s/ref-2-tim/ref-nt.2-tim/" $*-tmp.html
	sed -i '' "s/ref-titus/ref-nt.titus/" $*-tmp.html
	sed -i '' "s/ref-philem/ref-nt.philem/" $*-tmp.html
	sed -i '' "s/ref-heb/ref-nt.heb/" $*-tmp.html
	sed -i '' "s/ref-james/ref-nt.james/" $*-tmp.html
	sed -i '' "s/ref-1-pet/ref-nt.1-pet/" $*-tmp.html
	sed -i '' "s/ref-2-pet/ref-nt.2-pet/" $*-tmp.html
	sed -i '' "s/ref-1-jn/ref-nt.1-jn/" $*-tmp.html
	sed -i '' "s/ref-2-jn/ref-nt.2-jn/" $*-tmp.html
	sed -i '' "s/ref-3-jn/ref-nt.3-jn/" $*-tmp.html
	sed -i '' "s/ref-jude/ref-nt.jude/" $*-tmp.html
	sed -i '' "s/ref-rev/ref-nt.rev/" $*-tmp.html
	sed -i '' "s/draft: true/draft: false/" $*-tmp.html
	# sed '/>1000</{s/\(citation\">\)(\([^<]*\)\(<[^>]*>\)1000/\1(\3\2/;}' $*-tmp2.html > $*-tmp3.html
	# sed '/>1000</{s/\(citation\">\)(\([^<]*\)\(<[^>]*>\)1000<\/a>, \([^)]*)\)/\1(\3\2\4<\/a>/;}' $*-tmp2.html > $*-tmp3.html
	sed -i '' '/>1000</{s/\(citation\">\)(\([^<]*\)\(<a href=\"\)\([^-]*-\)\([^.]*\)\.\([^\"]*\)">1000<\/a>, \([^:]*\):\([^)]*\))/\1(\3https:\/\/www.lds.org\/scriptures\/\5\/\6\/\7\.\8\?lang=eng#\8">\2\7:\8<\/a>)/g;}' $*-tmp.html
	python ./aux/linkfix.py $*-tmp.html $*
	sed -i '' '/^<!DOCTYPE*/,/^<\/header>/{/^#/!{/^&/!d;};}' $*-tmp.html
	sed 's/ 1000.//g' $*-tmp.html > $@
	rm $*-tmp.html

clean:
	rm -f *.html *.pdf *.tex
