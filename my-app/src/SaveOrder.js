import React, { useContext, useState } from "react";
import { ListContext } from "./Context";

const SaveOrder = () => {
  const { list, saveOrder } = useContext(ListContext);
  const [selectedRange, setSelectedRange] = useState("");

  const handleRangeChange = (event) => {
    setSelectedRange(event.target.value);
  };

  const getUTCDate = (range) => {
    const today = new Date();
    let pastDate;
    switch (range) {
      case "0-3 months":
        pastDate = new Date(today.setMonth(today.getMonth() - 1));
        break;
      case "3-6 months":
        pastDate = new Date(today.setMonth(today.getMonth() - 4));
        break;
      case "6-12 months":
        pastDate = new Date(today.setMonth(today.getMonth() - 8));
        break;
      case "12-24 months":
        pastDate = new Date(today.setMonth(today.getMonth() - 16));
        break;
      default:
        pastDate = new Date();
    }
    return pastDate.toUTCString();
  };

  console.log(selectedRange);
  console.log(getUTCDate(selectedRange));

  return (
    <div>
      <select value={selectedRange} onChange={handleRangeChange}>
        <option value="">Select Date Range</option>
        <option value="0-3 months">0-3 months ago</option>
        <option value="3-6 months">3-6 months ago</option>
        <option value="6-12 months">6-12 months ago</option>
        <option value="12-24 months">12-24 months ago</option>
      </select>
      <button
        onClick={() => saveOrder(getUTCDate(selectedRange))}
        disabled={!selectedRange}
      >
        Save Order
      </button>
    </div>
  );
};

export default SaveOrder;
