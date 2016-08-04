# coding = UTF-8
import resource



rsrc = resource.RLIMIT_AS
soft, hard = resource.getrlimit(rsrc)
print(rsrc)
print(soft)
print(hard)
print(1024*1000000000*11)