const message = updateTaskStatus("T123", "In progress", true);

// Don't touch below this line

console.log(message);

function updateTaskStatus(taskId: string, currentStatus: string, isCompleted: boolean) {
  return new Promise((resolve) => {
    setTimeout(() => {
      if (currentStatus === 'In Progress') {
        if (isCompleted) {
          resolve(`Task ${taskId} has been completed successfully.`);
        } else {
          resolve(`Task ${taskId} is still in progress and cannot be completed.`);
        }
      } else {
        resolve(`Task ${taskId} status updated to ${currentStatus}.`);
      }
    }, 1000);
  });
}

export {};