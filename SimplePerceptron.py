import tensorflow as tf
import numpy as np
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [0], [0], [1]])  # Logical AND operation

# Define the perceptron model
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(1, activation='sigmoid', input_shape=(2,))  # One neuron with sigmoid activation
])

# Compile the model
model.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(X, y, epochs=100, verbose=0)

# Evaluate the model
loss, accuracy = model.evaluate(X, y)
print(f"Model Loss: {loss:.4f}")
print(f"Model Accuracy: {accuracy:.4f}")

# Make predictions
predictions = model.predict(X)
print("Predictions:", predictions.round())
