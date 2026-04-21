module.exports = {
  testEnvironment: "jsdom",
  setupFilesAfterEnv: ["<rootDir>/frontend/src/__tests__/jest.setup.js"],
  moduleNameMapper: {
    ".css$": "identity-obj-proxy"
  }
};
