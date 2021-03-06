from shovel import task

@task
def publish(title):
    '''
    Publish a draft.

    Call: `shovel publish filename`

    Takes the file "filename" (which *should* be in the _drafts directory) and
    live-ifies it...

    This is so I can just tab-complete the filename instead of remembering what
    it's called.
    '''

    import datetime, os, re, shutil
    from subprocess import call

    draft = title

    if os.path.isfile(draft):
        now = datetime.datetime.now()
        pubd =  "source/_posts/" + now.strftime("%Y/%m/%d/")

        if not os.path.exists(pubd):
            os.makedirs(pubd)

        pub = pubd + now.strftime("%Y-%m-%d-%H-%M-")
        pub += title[15:]

        print(pubd + " : " + pub)

        shutil.move(draft, pub)
        os.chdir("source")
        call(["git", "mv", draft, pub])

        #if shutil.move(draft, pub): print("moved") else: print("issue moving")
    else:
        print(str(title) + " could not be found. Looking for\n" + str(draft))
