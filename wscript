import Options
import platform
import os

srcdir = "."
blddir = "build"
APPNAME = "zookeeper"
OSTYPE = platform.system()


def set_options(opt):
    opt.tool_options("compiler_cxx")

def configure(conf):
    conf.check_tool("compiler_cxx")
    conf.check_tool("node_addon")

def build(bld):
    bld.exec_command("sh ../libzk-build.sh");

    includes = [bld.bdir + '/build/zk/include/zookeeper']
    libpaths = [bld.bdir + '/build/zk/lib']

    obj = bld.new_task_gen("cxx", "shlib", "node_addon")
#    if OSTYPE == 'Darwin':
#        obj.cxxflags = ["-Wall", "-Werror", '-DDEBUG', '-O0', '-mmacosx-version-min=10.4']
#        obj.ldflags = ['-mmacosx-version-min=10.4']
#    else:
#        # default build flags, add special cases if needed
    obj.cxxflags = ["-Wall", "-Werror", '-O0']
    obj.ldflags = ['']

    obj.target = "zookeeper"
    obj.source = "src/node-zk.cpp"
    obj.lib = ["zookeeper_st"]
    obj.includes = includes
    obj.libpath = libpaths

