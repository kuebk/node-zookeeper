import Options
import platform
import os

def set_options(opt):
    opt.tool_options("compiler_cxx")

def configure(conf):
    conf.check_tool("compiler_cxx")
    conf.check_tool("node_addon")

def build(bld):
    bld.exec_command("sh ../libzk-build.sh");

    includes = [bld.bdir + '/zookeeper/include/zookeeper']
    libpaths = [bld.bdir + '/zookeeper/lib']

    obj = bld.new_task_gen("cxx", "shlib", "node_addon")
    obj.cxxflags = ["-Wall", "-Werror", '-O0']
    obj.ldflags = ['']

    obj.target = "zookeeper"
    obj.source = "src/node-zk.cpp"
    obj.lib = ["zookeeper_st"]
    obj.includes = includes
    obj.libpath = libpaths
