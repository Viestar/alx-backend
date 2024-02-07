import { createClient, print } from 'redis';

const client = createClient();

client
  .on("connect", () => {
    console.log("Redis client connected to the server");
  })
  .on("error", (error) => {
    console.log(`Redis client not connected to the server: ${error}`);
  });

// Function to set multiple fields in a hash
function setHashFields(hashName, fields) {
  Object.entries(fields).forEach(([field, value]) => {
    client.hset(hashName, field, value, print);
  });
}

// Define the hash fields and their values
const hashFields = {
  'Portland': 50,
  'Seattle': 80,
  'New York': 20,
  'Bogota': 20,
  'Cali': 40,
  'Paris': 2
};

// Create Hash
setHashFields('HolbertonSchools', hashFields);

// Display Hash
client.hgetall('HolbertonSchools', (err, reply) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(reply);
});

