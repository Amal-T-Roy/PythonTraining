#include<Python.h>

void main()
{

//Initialise
Py_Initialize();

//Create file pointer of python script
FILE* fp = fopen("module_name.py","r");

//Run file
PyRun_SimpleFile(fp,"module_name.py");

/*
PyObject* module = PyImport_ImportModule("module_name ");
PyObject* function = PyObject_GetAttrString(module, "function_name ");
*/

PyObject* module = PyImport_ImportModule("module_name");
PyObject* dict = PyModule_GetDict(module);
PyObject* function = PyDict_GetItemString(dict, "function_name");

// call the function and get its return value
    PyObject* args = PyTuple_New(0);
    //PyObject* result = PyObject_CallObject(function, args);
    PyObject* result = PyObject_CallFunction(function, NULL);

    // print the result
    printf("The result is %ld\n", PyLong_AsLong(result));

fclose(fp);


Py_DECREF(result);
Py_DECREF(function);
Py_DECREF(module);

//Close
Py_Finalize(); 

}
