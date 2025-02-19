"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var message = updateTaskStatus("T123", "In progress", true);
// Don't touch below this line
console.log(message);
function updateTaskStatus(taskId, currentStatus, isCompleted) {
    return new Promise(function (resolve) {
        setTimeout(function () {
            if (currentStatus === 'In Progress') {
                if (isCompleted) {
                    resolve("Task ".concat(taskId, " has been completed successfully."));
                }
                else {
                    resolve("Task ".concat(taskId, " is still in progress and cannot be completed."));
                }
            }
            else {
                resolve("Task ".concat(taskId, " status updated to ").concat(currentStatus, "."));
            }
        }, 1000);
    });
}
