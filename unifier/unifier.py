import shutil, os, hashlib

already_seen = set()

def add_from_prefix(prefix, fprefix=''):
    print 'working on', prefix
    for dname in os.listdir(prefix):
        if os.path.isdir(prefix+dname):
            print dname
            for fname in os.listdir(prefix + dname):
                fullfn = prefix + dname + '/' + fname
                h = hashlib.sha256(open(fullfn, 'rb').read())
                if (h.hexdigest() not in already_seen):
                    shutil.copyfile(fullfn, 'replays/' + dname + '/' + fprefix + fname)
                    already_seen.add(h.hexdigest())
                    print 'added: ', fullfn
                else:
                    print 'already seen: ', fullfn

def seen(replay_path):
    h = hashlib.sha256(open(replay_path, 'rb').read())
    if (h.hexdigest() not in already_seen):
        already_seen.add(h.hexdigest())
        print ' + added:', replay_path, ' : ', h.hexdigest()[0:7]
    else:
        print ' -- already seen: ', replay_path

def add(replay_path):
    print 'working on', replay_path
    for dname in os.listdir(replay_path):
        print 'dname:', dname
        if os.path.isdir(replay_path + dname):
            print "esta es una carpeta y se llama: " + dname
            for fname in os.listdir(replay_path + "/" + dname):
                print 'fname:', fname
                seen(replay_path + dname + "/" + fname)
        else:
            seen(replay_path + dname)


if __name__ == '__main__':
    add('../teamliquid/replays/')
    #add_from_prefix('replays/', 'HERE')
    #add_from_prefix('../iccup/iccup_users/', 'IC')
    #add_from_prefix('../iccup_users/', 'IC')
    #add_from_prefix('../iccup/replays/', 'IC')
    #add_from_prefix('../iccup_gosus/', 'IC')
    #add_from_prefix('../teamliquid/replays/', 'TL')
    #add_from_prefix('../gosugamers/replays/', 'GG')

