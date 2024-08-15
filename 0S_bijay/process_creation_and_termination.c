#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

int main() {
    STARTUPINFO si;
    PROCESS_INFORMATION pi;

    ZeroMemory(&si, sizeof(si));
    si.cb = sizeof(si);
    ZeroMemory(&pi, sizeof(pi));

    // Create child process
    if (!CreateProcess(NULL,                // No module name (use command line)
                       "child_process.exe", // Command line for child process
                       NULL,                // Process handle not inheritable
                       NULL,                // Thread handle not inheritable
                       FALSE,               // Set handle inheritance to FALSE
                       0,                   // No creation flags
                       NULL,                // Use parent's environment block
                       NULL,                // Use parent's starting directory
                       &si,                 // Pointer to STARTUPINFO structure
                       &pi)                 // Pointer to PROCESS_INFORMATION structure
       ) {
        printf("CreateProcess failed (%d).\n", GetLastError());
        return 1;
    }

    // Parent process continues here
    printf("This is the parent process.\n");

    // Get the Process ID of the child process
    DWORD childPID = GetProcessId(pi.hProcess);
    if (childPID == 0) {
        printf("Failed to get child process ID.\n");
    } else {
        printf("Child process ID: %lu\n", childPID);
    }

    // Wait until child process exits
    WaitForSingleObject(pi.hProcess, INFINITE);

    // Close process and thread handles
    CloseHandle(pi.hProcess);
    CloseHandle(pi.hThread);

    printf("Exiting the program.\n");
    return 0;
}

