import shelve, pyperclip, sys
mcbShelf = shelve.open('mcb')
# TODO: Save clipboard content.
# TODO: List keywords and load content.
# mcbShelf.close()
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
        print(list(mcbShelf))
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcbShelf(sys.argv[2])
mcbShelf.close()