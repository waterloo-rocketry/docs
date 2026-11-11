****************************
Canards Firmware Development
****************************

Lines of Code Statistics
========================

.. image:: https://csclub.uwaterloo.ca/~j9xu/cansw_canards-loc.svg

.. _docstring_standards_embedded_c:


Docstring Standards for Embedded C
=========================================

Docstrings are mandated for controls firmware development to generate context for development. 

=========================================
1. Header Function Docstrings
=========================================

Header file documentation defines the **interface contract** for external callers. 
It must specify memory constraints, alignment requirements, hardware dependencies, and exact return states, if applicable. 

Google is your best resource when it comes to what keywords to use. Some common examples are: 
  * **@brief**: A concise sentence describing what the function does.
  * **@details**: Architectural notes, hardware behaviors, or driver-level constraints.
  * **@pre**: Preconditions that must be met before calling (e.g., initialization checks, buffer alignment).
  * **@param[in/out]**: Directional parameter descriptions, explicitly stating memory location requirements (e.g., DMA-accessible memory).
  * **@return**: Explicit enumeration of all possible return codes.
  * **@satisfies**: Traceability tags linking implementation to system requirements.

Example Header Docstring:

.. code-block:: c

    /**
     * @brief Reads data synchronously from the specified byte address on the SD card.
     *
     * @details Handles cache line invalidation and internal read timeout management 
     *          via the underlying SDMMC HAL layer.
     *
     * @pre raw_logger_SD_init() must have completed successfully.
     * @pre Buffer must be 32-byte aligned for DMA operations.
     * @pre Buffer must reside in IDMA-accessible memory (non-DTCM).
     * @pre byte_address and num_bytes must be 512-byte aligned.
     *
     * @param[out] buffer       Pointer to the destination buffer.
     * @param[in]  byte_address Target byte offset on the card (512-byte aligned).
     * @param[in]  num_bytes    Total bytes to read; must be a non-zero multiple of 512.
     * @param[in]  timeout      Maximum milliseconds to wait for driver availability.
     *
     * @return w_status_t 
     *         - W_SUCCESS: Read completed successfully.
     *         - W_FAILURE: Driver not initialized or in recovery state.
     *         - W_INVALID_PARAM: Parameters violated alignment or null pointer checks.
     *         - W_IO_TIMEOUT: Operation timed out.
     *
     * @satisfies REQ_RAW_LOG_012
     */
    w_status_t raw_logger_SD_read(uint8_t *buffer, uint32_t byte_address, uint32_t num_bytes,
                                  uint32_t timeout);

=========================================
2. Static Function Docstrings
=========================================

Docstrings for static functions shall be placed **above** the function definition in the source file. 

Example Static Function Docstring:

.. code-block:: c

    /**
     * @brief Resets internal DMA streams and clears error flags on the SDMMC peripheral.
     *
     * @note Must be called only while holding the raw_sd_mutex to prevent concurrent 
     *       register modification across threads.
     *
     * @param[in] p_handle Pointer to the active SD HAL handle.
     * @return true if hardware recovery sequence completed; false otherwise.
     */
    static bool prv_sd_reset_dma_stream(SD_HandleTypeDef *p_handle) {
        // Implementation 
    }

=========================================
3. Syntax Rules Summary
=========================================

1. **Use standard block comment formatting**: Open with `/**` and prefix subsequent lines with ` * ` (aligned with the asterisk).
2. **Never use leading hyphens (`-`)**: Hyphens break Doxygen and Sphinx parsers, turning structured tags into plain text.
3. **Explicitly document memory constraints**: In embedded systems, pointer parameters must state alignment requirements (`32-byte aligned`), memory regions (`non-DTCM`), and null-pointer behavior.