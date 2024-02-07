import { createQueue } from 'kue';
const queue = kue.createQueue();

// Create an object containing the job data
const jobData = {
  phoneNumber: '0775056439',
  message: 'Hello!',
};

// Creating a queue named push_notification_code and create a job with the provided data
const job = queue.create('push_notification_code', jobData)
  .save((err) => {
    if (err) {
      console.error('Notification job failed');
      return;
    }
    console.log('Notification job created:', job.id);
  });

// Listening for job completion
job.on('complete', () => {
  console.log('Notification job completed');
});

// Listening for job failure
job.on('failed', () => {
  console.log('Notification job failed');
});
