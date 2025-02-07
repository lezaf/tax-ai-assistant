import { describe, it, expect, vi } from "vitest";
import { mount } from "@vue/test-utils";
import TaxForm from "@/components/TaxForm.vue";
import axios from "axios";

vi.mock("axios"); // Mock axios to prevent actual API calls

afterEach(() => {
  vi.clearAllMocks(); // Clears mock history
});

describe("TaxForm Form Submission", () => {
  it("should submit form if validation succeeds", async () => {
    const wrapper = mount(TaxForm);

    // Set valid data
    wrapper.vm.taxData.income = 20000;
    wrapper.vm.taxData.expenses = 2000;
    wrapper.vm.taxData.propertiesNum = 2;
    wrapper.vm.taxData.userPrompt = "Any advice to reduce my taxes?";

    // Mock API response
    axios.post.mockResolvedValue({
      data: {
        answer: "To reduce your taxes I would...",
      },
    });

    // Submit form
    await wrapper.find("form").trigger("submit.prevent");

    // Check API call was made with expected data
    expect(axios.post).toHaveBeenCalledWith(
      "http://localhost:8000/api/advice/generate",
      {
        userData: {
          income: 20000,
          expenses: 2000,
          propertiesNum: 2,
        },
        userPrompt: "Any advice to reduce my taxes?",
      },
      {
        headers: { "Content-Type": "application/json" },
      }
    );
  });

  it("should not submit form if validation fails", async () => {
    const wrapper = mount(TaxForm);

    // Set invalid data
    wrapper.vm.taxData.income = -20000;
    wrapper.vm.taxData.expenses = 2000;
    wrapper.vm.taxData.propertiesNum = 2;
    wrapper.vm.taxData.userPrompt = "Any advice to reduce my taxes?";

    // Trye to submit form
    await wrapper.find("form").trigger("submit.prevent");

    // API should not be called because validation failed
    expect(axios.post).not.toHaveBeenCalled();
  });
});
