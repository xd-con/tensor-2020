.PHONY: github html clean serve poster

html:
	@cd site && hugo
	@touch site/public/.nojekyll

serve:
	@cd site && hugo server -D

clean:
	@rm -rf site/public

github: | clean html
	./push_dir_to_repo.py \
	  --branch gh-pages \
	  --email web@xd-con.org \
	  --committer "xd-web" \
	  --message "Update website" \
	  --force \
	     ./site/public git@github.com:xd-con/tensor-2020

poster:
	cd admin/poster && \
	cp poster-header.md poster.md && \
	python ../../tools/schedule_to_md.py >> poster.md && \
	pandoc poster.md --pdf-engine=xelatex -H preamble.tex -o poster.pdf
