TARGET := $(word 1, $(MAKECMDGOALS))
ID := $(word 2, $(MAKECMDGOALS))
NAME := $(wordlist 3, $(words $(MAKECMDGOALS)), $(MAKECMDGOALS))

SLUG := $(shell echo "$(NAME)" | tr '[:upper:]' '[:lower:]' | tr ' ' '-')

desafio:
	mkdir -p $(ID)-$(SLUG)
	touch $(ID)-$(SLUG)/statement.txt
	touch $(ID)-$(SLUG)/input.txt
	touch $(ID)-$(SLUG)/output.txt
	touch $(ID)-$(SLUG)/solution.py

%:
	@:
