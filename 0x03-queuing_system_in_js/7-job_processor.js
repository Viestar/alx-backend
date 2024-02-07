import { createQueue, Job } from 'kue';
const queue = createQueue();

// Defining blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Defining the sendNotification function
function sendNotification(phoneNumber, message, job, done) {
  // Tracking job progress
  job.progress(0, 100);

  // Checking if phoneNumber is blacklisted
  if (blacklistedNumbers.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  // Tracking job progress
  job.progress(50);

  // Loging notification
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

  // Tracking job progress
  job.progress(100);

  // Notifying job completion
  done();
}

// Processing jobs from push_notification_code_2 queue
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});

console.log('Job processor is running...');

