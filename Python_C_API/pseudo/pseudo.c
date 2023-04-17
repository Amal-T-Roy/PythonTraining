#include <Python.h>
#include <stdio.h>

int main() {
    Py_Initialize();

    PyObject* pModule = PyImport_ImportModule("module_name");
    PyObject* pFunc = PyObject_GetAttrString(pModule, "function_name");
    /*
    PyObject* pArgs = PyTuple_New(2);
    PyTuple_SetItem(pArgs, 0, PyLong_FromLong(123));
    PyTuple_SetItem(pArgs, 1, PyUnicode_FromString("hello"));
    */
    PyObject* pResult = PyObject_CallObject(pFunc, NULL);
    
    int result = PyLong_AsLong(pResult);
    printf("Result = %d\n",result);

    //Py_DECREF(pArgs);
    Py_DECREF(pFunc);
    Py_DECREF(pModule);
    Py_DECREF(pResult);
    Py_Finalize();

    return 0;
}

